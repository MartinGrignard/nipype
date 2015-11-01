# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..dti import DTLUTGen


def test_DTLUTGen_inputs():
    input_map = dict(acg=dict(argstr='-acg',
    ),
    args=dict(argstr='%s',
    ),
    bingham=dict(argstr='-bingham',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    frange=dict(argstr='-frange %s',
    position=1,
    units='NA',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inversion=dict(argstr='-inversion %d',
    units='NA',
    ),
    lrange=dict(argstr='-lrange %s',
    position=1,
    units='NA',
    ),
    out_file=dict(argstr='> %s',
    genfile=True,
    position=-1,
    ),
    samples=dict(argstr='-samples %d',
    units='NA',
    ),
    scheme_file=dict(argstr='-schemefile %s',
    mandatory=True,
    position=2,
    ),
    snr=dict(argstr='-snr %f',
    units='NA',
    ),
    step=dict(argstr='-step %f',
    units='NA',
    ),
    terminal_output=dict(nohash=True,
    ),
    trace=dict(argstr='-trace %G',
    units='NA',
    ),
    watson=dict(argstr='-watson',
    ),
    )
    inputs = DTLUTGen.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_DTLUTGen_outputs():
    output_map = dict(dtLUT=dict(),
    )
    outputs = DTLUTGen.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
