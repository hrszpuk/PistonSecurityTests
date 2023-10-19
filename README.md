# Piston Security Tests
This repository is dedicated to testing the security claims that [Piston]() makes.
These tests assume you have a local piston api instance running on `localhost:2000`.

To start the tests, run the `run.py` file.
Each Python file with the prefix `test_` will be read, and fed into piston.
The results of the test will be displayed on the command line.

### Tests
We test each of Piston's security claims:
- [ ] Disabling outgoing network interaction
- [ ] Capping max processes at 256 by default
- [ ] Capping max files at 2048 (resists various file-based attacks)
- [ ] Cleaning up all temp space after each execution (resists out of drive space attacks)
- [ ] Running as a variety of unprivileged users
- [ ] Capping runtime execution at 3 seconds
- [ ] Capping stdout to 65536 characters (resists yes/no bombs and runaway output)
- [ ] SIGKILLing misbehaving code


