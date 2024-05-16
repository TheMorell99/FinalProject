# Punt entrada aplicació
"""
Usage:
python3 main.py --c <config_file>

Help:
python3 main.py --help
"""

import click, yaml
from farm import Farm


@click.command()
@click.option('--c', default="config.yaml", type=click.Path("rb"), help="help")
def get_config(c):
    """
    Load and return the configuration from the specified file.

    Args:
        c (str): The path to the configuration file.

    Returns:
        dict: The loaded configuration.

    """
    with open(c) as config_file:
        cfg = yaml.load(config_file, Loader=yaml.FullLoader)
    return cfg



if __name__ == "__main__":
    """
        Main function that starts the farm.
        We get the configuration from the config file and start the farm.
    """
    
    cfg = get_config.main(standalone_mode=False)
    farm = Farm(cfg=cfg)
    farm.start()
    



