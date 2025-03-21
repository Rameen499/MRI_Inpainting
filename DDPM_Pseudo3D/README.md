# Inpainting of Healthy Brain Tissue using 2.5D Diffusion Models



## Training

To train the model, run

```
python3 scripts/inpainting_train.py --data_dir ./data/training --log_dir ./model $TRAIN_FLAGS $MODEL_FLAGS $DIFFUSION_FLAGS

--data_dir        : training data directory
--log_dir         : where model checkpoints saved
