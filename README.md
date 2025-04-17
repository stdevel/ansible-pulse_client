# pulse_client

Installs the Ivanti Pulse Connect Secure VPN client.

## Requirements

No requirements.

## Role Variables

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `pulse_filename` | *some URL* | Package file to install |
| `pulse_ubuntu_workaround` | `false` | Temporarily enable Ubuntu 22.04 repositories for some missing libraries (see below) |

Check-out the [vars/*.yml](vars/) files - there is a list of alternate download sites.

## Dependencies

No dependencies.

## Example Playbook

Local file installation:

```yaml
---
- hosts: clients
  roles:
    - role: stdevel.pulse_client
      pulse_filename: pulsesecure_9.1.R13_amd64.deb
```

Repository installation:

```yaml
---
- hosts: clients
  roles:
    - role: stdevel.pulse_client
      pulse_filename: https://simone.giertz.dev/foobar/pulsesecure_13.17.rpm
```

Use the Ubuntu workaround. Current Pulse Secure versions still require some libraries (`libwebkit2gtk-4.0`, `libjavascriptcoregtk`, `libicu70`) not available to Ubuntu releases newer than 22.04:

```yaml
---
- hosts: clients
  roles:
    - role: stdevel.pulse_client
      pulse_filename: ps-pulse-linux-22.8r1-b31437-64bit-installer.deb
      pulse_ubuntu_workaround: true
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
