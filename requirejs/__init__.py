from .execjs import execjs
import os


class RJSException(Exception):
    pass


def optimize(conf=None, working_directory=None, **kwargs):
    if conf is None:
        conf = kwargs
    if working_directory is None:
        working_directory = "."
    if 'dir' in conf:
        write_dir = os.path.join(working_directory, conf['dir'])
    else:
        write_dir = None

    result, log = execjs(
        filename="r.js",
        method="optimize",
        argument=conf,
        callback=True,
        argv=['-o', 'dummy.json'],
        base_dir=working_directory,
        write_dir=write_dir,
    )
    if log and "Error" in log[-1]:
        raise RJSException(log[-1])
    else:
        return result
