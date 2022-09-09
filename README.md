# pulse_client

Installs the Ivanti Pulse Connect Secure VPN client.

## Requirements

No requirements.

## Role Variables

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `pulse_filename` | *some government site* | Package file to install |
| `pulse_os_network_service` | *preset, see [vars/*.yml](vars/)* | Network service (e.g. `NetworkManager`), required for `systemd-resolved` incompatibility |

Check-out the [vars/*.yml](vars/) files - there is a list of alternate download sites.

## Dependencies

No dependencies.

## Example Playbook

Local file installation:

```yaml
- hosts: clients
  roles:
    - role: stdevel.pulse_client
      pulse_filename: pulsesecure_9.1.R13_amd64.deb
```

Repository installation:

```yaml
- hosts: clients
  roles:
    - role: stdevel.pulse_client
      pulse_filename: https://simone.giertz.dev/foobar/pulsesecure_13.17.rpm
```

## Development / Testing

Use [Ansible Molecule](https://molecule.readthedocs.io/en/latest/index.html) for running tests:

```shell
$ molecule create
$ molecule converge
```

Run the tests:

```shell
$ molecule verify
```

## License

BSD

## Author Information

Christian Stankowic
