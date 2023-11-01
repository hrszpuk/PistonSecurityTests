# Piston Security Tests
This repository is dedicated to testing the security claims that [Piston]() makes.
These tests assume you have a local piston api instance running on `localhost:2000`.

To start the tests, run the `test_run.py` file.
Each Python unittest will be read sample code from the `test_code` folder, and feed it into piston.
The results of the test will be displayed on the command line.

### Tests
We test each of Piston's security claims:
- [x] Disabling outgoing network interaction
- [x] Capping max processes at 256 by default
- [x] Capping max files at 2048 (resists various file-based attacks)
- [x] Capping runtime execution at 3 seconds
- [x] Capping stdout to 65536 characters (resists yes/no bombs and runaway output)

### Observations
We may observe the SIGKILLing of misbehaving code; these cases cause a mostly empty response with the value of the `code` field being `SIGKILL`.
