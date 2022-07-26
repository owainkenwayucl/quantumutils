# Build Tools

This directory includes some useful command-line tools whose functionality is missing from the MyQLM distribution.

## `circ2job`

This command line tool converts a circuit into a job file.  For reasons that are not clear, the MyQLM documentation tells you to do this in Python and doesn't provide a tool.  This is that tool, written in python:

```
usage: circ2job [-h] [-o filename] circuit

Convert circuits to jobs.

positional arguments:
  circuit

optional arguments:
  -h, --help   show this help message and exit
  -o filename  Output file.
```

Thus the sequence to convert an AQASM file into a job is as follows:

```
$ aqasm2circ test.aqasm test.circ
$ circ2job test.circ
$ qat-jobrun --qpu qat.pylinalg:PyLinalg test.circ.job
```

## `qc`

The `qc` tool is a script that wraps up the entire process of taking an AQASM file and outputing either a job or a batch job.

For licensing reasons, this calls `aqasm2circ` via `subprocess` because whatever mechanism `aqasm2circ` uses within MyQLM is undocumented and therefore presumably closed source.

```
usage: qc [-h] [-o filename] [-b] [--full-matrices] [--no-default-gateset] [--no-inline]
          [-L module]
          aqasm

Compile AQASM to jobs.

positional arguments:
  aqasm

optional arguments:
  -h, --help            show this help message and exit
  -o filename           Output file.
  -b                    Generate a batch file instead.
  --full-matrices       Passed to aqasm2circ. See aqasm2circ --help for details.
  --no-default-gateset  Passed to aqasm2circ. See aqasm2circ --help for details.
  --no-inline           Passed to aqasm2circ. See aqasm2circ --help for details.
  -L module             Passed to aqasm2circ. See aqasm2circ --help for details.

```

The process for compiling and running an AQASM file with `qc` is:

```
$ qc test.aqasm 
$ qat-jobrun --qpu qat.pylinalg:PyLinalg test.aqasm.job
```

## Installation

To install these, just put them somewhere in `$PATH`.  To keep things neat on my system I've put them in the `bin` folder in my MyQLM conda.
