import hydra
from omegaconf import OmegaConf,DictConfig

@hydra.main(version_base=None,config_path='config',config_name='config')
def test(cfg : DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))
    
test()