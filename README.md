# Piston Security Tests

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


