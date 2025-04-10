===================
Asset Force Account
===================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:f883b5ebc3a9f6c0466601bb1e7dc73cb3d3b71291c41104037eb41ac81049df
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Faccount--financial--tools-lightgray.png?logo=github
    :target: https://github.com/OCA/account-financial-tools/tree/17.0/account_asset_force_account
    :alt: OCA/account-financial-tools
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/account-financial-tools-17-0/account-financial-tools-17-0-account_asset_force_account
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/account-financial-tools&target_branch=17.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module enables the ability to override default accounts directly
from the asset form.

**Table of contents**

.. contents::
   :local:

Usage
=====

1. | **Create an Asset Profile**:
   | Navigate to **Configuration -> Asset Profiles** and create a new
     profile.

2. **Create a Vendor Bill**:

   - Go to **Vendors -> Bills** and create a new bill.
   - Add a product and select the asset profile you just created.
   - The Asset Account will be derived from the profile or can be
     manually updated at this step (the invoice account will be used as
     the Asset Account).
   - Set the product price and confirm the bill.

3. | **Asset Creation**:
   | Once the bill is confirmed, the asset will be created and populated
     with the associated accounts. You can now manually adjust the
     **Depreciation Account** and **Depreciation Expense Account** if
     necessary.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/account-financial-tools/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/account-financial-tools/issues/new?body=module:%20account_asset_force_account%0Aversion:%2017.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
-------

* Bernat Obrador (APSL-Nagarro)

Contributors
------------

- `APSL-Nagarro <https://apsl.tech>`__:

  - Bernat Obrador <bobrador@apsl.net>

Maintainers
-----------

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-BernatObrador| image:: https://github.com/BernatObrador.png?size=40px
    :target: https://github.com/BernatObrador
    :alt: BernatObrador

Current `maintainer <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-BernatObrador| 

This module is part of the `OCA/account-financial-tools <https://github.com/OCA/account-financial-tools/tree/17.0/account_asset_force_account>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
