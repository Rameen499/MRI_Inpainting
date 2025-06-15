import streamlit as st
import nibabel as nib
import numpy as np
import tempfile
import os

st.set_page_config(page_title="MRI Inpainting Demo", layout="wide")
st.title("🧠 MRI Inpainting Demo (No Model Yet)")

uploaded_file = st.file_uploader("Upload a `.nii` or `.nii.gz` file", type=["nii", "nii.gz"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".nii.gz") as tmp:
        tmp.write(uploaded_file.read())
        file_path = tmp.name

    nii = nib.load(file_path)
    volume = nii.get_fdata()
    st.success(f"Loaded MRI with shape: {volume.shape}")

    slice_idx = st.slider("Select slice", 0, volume.shape[2] - 1, volume.shape[2] // 2)
    original = volume[:, :, slice_idx]
    inpainted = np.max(original) - original  # Dummy "inpainting"

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Original Slice")
        st.image(original, clamp=True, use_column_width=True)
    with col2:
        st.subheader("Mock Inpainted Slice")
        st.image(inpainted, clamp=True, use_column_width=True)

    if st.button("Save dummy inpainted volume"):
        result_vol = volume.copy()
        result_vol[:, :, slice_idx] = inpainted
        out = nib.Nifti1Image(result_vol, affine=nii.affine)
        out_path = "inpainted_output.nii.gz"
        nib.save(out, out_path)
        with open(out_path, "rb") as f:
            st.download_button("⬇️ Download .nii.gz", f, file_name="inpainted_output.nii.gz")
