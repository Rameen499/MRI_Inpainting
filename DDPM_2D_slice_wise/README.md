
# Inpainting of Healthy Brain Tissue using 2D slice-wise Diffusion Models

Baseline model


## Training

To train the model, run

```
python3 scripts/inpainting_train.py --data_dir ./data_3d/training --log_dir ./model $TRAIN_FLAGS $MODEL_FLAGS $DIFFUSION_FLAGS

--data_dir        : training data directory
--log_dir         : where model checkpoints saved

```

## Sampling

To generate samples using the trained model, run

```
python scripts/inpainting_sample.py  --data_dir ./test_data --log_dir ./sampling_results --model_path ./model/savedmodel325000.pt --adapted_samples ./sampling_results_adapted $MODEL_FLAGS $DIFFUSION_FLAGS

--data_dir        : directory of the test data
--log_dir         : output directory
--model_path      : where model is saved
--adapted_samples : where post processed files are saved (post processing as required for the evaluation)

optional: --gt_dir ./test_data_gt 
--gt_dir          : directory of ground truth images corresponding to testing data (if eval_sam is used in file inpainting_sample.py, line 201)
```
