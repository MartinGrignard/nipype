# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..model import SMM


def test_SMM_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    mask=dict(argstr='--mask="%s"',
    copyfile=False,
    mandatory=True,
    position=1,
    ),
    no_deactivation_class=dict(argstr='--zfstatmode',
    position=2,
    ),
    output_type=dict(),
    spatial_data_file=dict(argstr='--sdf="%s"',
    copyfile=False,
    mandatory=True,
    position=0,
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = SMM.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_SMM_outputs():
    output_map = dict(activation_p_map=dict(),
    deactivation_p_map=dict(),
    null_p_map=dict(),
    )
    outputs = SMM.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
