import torch
from torchvision.models import resnet18, ResNet18_Weights

try:
    model = resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)
    model.eval()
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Model loading error: {e}")