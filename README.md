Traceback (most recent call last):
  File "C:\Users\joyjosj\PycharmProjects\PythonProject\main.py", line 1, in <module>
    from ultralytics import YOLO
  File "C:\Users\joyjosj\AppData\Local\miniforge3\envs\yolo\Lib\site-packages\ultralytics\__init__.py", line 11, in <module>
    from ultralytics.models import NAS, RTDETR, SAM, YOLO, YOLOE, FastSAM, YOLOWorld
  File "C:\Users\joyjosj\AppData\Local\miniforge3\envs\yolo\Lib\site-packages\ultralytics\models\__init__.py", line 3, in <module>
    from .fastsam import FastSAM
  File "C:\Users\joyjosj\AppData\Local\miniforge3\envs\yolo\Lib\site-packages\ultralytics\models\fastsam\__init__.py", line 3, in <module>
    from .model import FastSAM
  File "C:\Users\joyjosj\AppData\Local\miniforge3\envs\yolo\Lib\site-packages\ultralytics\models\fastsam\model.py", line 6, in <module>
    from ultralytics.engine.model import Model
  File "C:\Users\joyjosj\AppData\Local\miniforge3\envs\yolo\Lib\site-packages\ultralytics\engine\model.py", line 8, in <module>
    import torch
  File "C:\Users\joyjosj\AppData\Local\miniforge3\envs\yolo\Lib\site-packages\torch\__init__.py", line 2016, in <module>
    from torch import _VF as _VF, functional as functional  # usort: skip
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\joyjosj\AppData\Local\miniforge3\envs\yolo\Lib\site-packages\torch\functional.py", line 7, in <module>
    import torch.nn.functional as F
  File "C:\Users\joyjosj\AppData\Local\miniforge3\envs\yolo\Lib\site-packages\torch\nn\__init__.py", line 8, in <module>
    from torch.nn.modules import *  # usort: skip # noqa: F403
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\joyjosj\AppData\Local\miniforge3\envs\yolo\Lib\site-packages\torch\nn\modules\__init__.py", line 1, in <module>
    from .module import Module  # usort: skip
    ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\joyjosj\AppData\Local\miniforge3\envs\yolo\Lib\site-packages\torch\nn\modules\module.py", line 29, in <module>
    from torch.utils._python_dispatch import is_traceable_wrapper_subclass
  File "C:\Users\joyjosj\AppData\Local\miniforge3\envs\yolo\Lib\site-packages\torch\utils\__init__.py", line 8, in <module>
    from torch.utils import (
  File "C:\Users\joyjosj\AppData\Local\miniforge3\envs\yolo\Lib\site-packages\torch\utils\data\__init__.py", line 1, in <module>
    from torch.utils.data.dataloader import (
  File "C:\Users\joyjosj\AppData\Local\miniforge3\envs\yolo\Lib\site-packages\torch\utils\data\dataloader.py", line 20, in <module>
    import torch.distributed as dist
  File "C:\Users\joyjosj\AppData\Local\miniforge3\envs\yolo\Lib\site-packages\torch\distributed\__init__.py", line 122, in <module>
    from .device_mesh import DeviceMesh, init_device_mesh
  File "C:\Users\joyjosj\AppData\Local\miniforge3\envs\yolo\Lib\site-packages\torch\distributed\device_mesh.py", line 64, in <module>
    class _MeshEnv(threading.local):
  File "C:\Users\joyjosj\AppData\Local\miniforge3\envs\yolo\Lib\site-packages\torch\distributed\device_mesh.py", line 282, in _MeshEnv
    pg_options: Optional[ProcessGroup.Options] = None,
                         ^^^^^^^^^^^^^^^^^^^^
AttributeError: type object 'torch._C._distributed_c10d.ProcessGroup' has no attribute 'Options'
