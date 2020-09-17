[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-cloc.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-cloc) ![Ansible Role](https://img.shields.io/ansible/role/47891?color=dark%20green) ![Ansible Role](https://img.shields.io/ansible/role/d/47891?color=dark&style=flat-square) ![Ansible Quality Score](https://img.shields.io/ansible/quality/47891?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-cloc&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-cloc) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-cloc?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-cloc?color=orange&style=flat-square)

# Ansible Role: cloc

Role to install (_by default_) [cloc](https://github.com/AlDanial/cloc) or uninstall (_if passed as var_) on Debian based and EL based systems. As per the official statement on the repository's GitHub page, it allows for "_cloc counts blank lines, comment lines, and physical lines of source code in many programming languages._"

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
cloc_app: cloc
cloc_desired_state: present
```

### Variables table:

Variable           | Value (default) | Description
------------------ | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------
cloc_app           | cloc            | Defines the app to install i.e. **cloc**
cloc_desired_state | present         | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **cloc** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.cloc
```

For customizing behavior of role (i.e. installation of latest **cloc** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.cloc
  vars:
    cloc_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **cloc** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.cloc
  vars:
    cloc_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-cloc/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
