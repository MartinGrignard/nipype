# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..base import AFNICommand


def test_AFNICommand_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    out_file=dict(argstr='-prefix %s',
    name_source=['in_file'],
    name_template='%s_afni',
    ),
    outputtype=dict(),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = AFNICommand.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

