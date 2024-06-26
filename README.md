[![build-test](https://github.com/darkwizard242/ansible-role-cloc/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-cloc/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-cloc/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-cloc/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/cloc) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-cloc&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-cloc) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-cloc&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-cloc) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-cloc&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-cloc) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-cloc?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-cloc?color=orange&style=flat-square)

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

Variable           | Description
------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------
cloc_app           | Defines the app to install i.e. **cloc**
cloc_desired_state | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`.

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

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
