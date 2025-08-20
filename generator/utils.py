from generator.hy3dgen.shapegen.pipelines import Hunyuan3DDiTFlowMatchingPipeline

def generate_mesh(image, model_path="Tencent-Hunyuan/Hunyuan3D-2"):
    pipeline = Hunyuan3DDiTFlowMatchingPipeline.from_pretrained(model_path)
    mesh = pipeline(image=image, num_inference_steps=30)[0]
    return mesh
