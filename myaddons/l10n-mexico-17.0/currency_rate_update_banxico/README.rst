=============================
Currency Rate Update: Banxico
=============================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:d38ca566aaefdf79f44d76fd85c85c422498ec0d2475bb239a5afafbaa41cdbb
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fl10n--mexico-lightgray.png?logo=github
    :target: https://github.com/OCA/l10n-mexico/tree/17.0/currency_rate_update_banxico
    :alt: OCA/l10n-mexico
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/l10n-mexico-17-0/l10n-mexico-17-0-currency_rate_update_banxico
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/l10n-mexico&target_branch=17.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module adds `Banxico <https://www.banxico.org.mx/>`__ currency
exchange rate web services.

**Table of contents**

.. contents::
   :local:

Configuration
=============

Now you can choose the 'Bank of Mexico' service when configuring a
currency rates providers.

1. Go to Banxico to `generate a
   token <https://www.banxico.org.mx/SieAPIRest/service/v1/token>`__.
2. Go to *Invoicing > Configuration > Currency Rates Providers*.
3. Create a new 'Currency Rates Providers' or edit an existing one and
   you will see 'Bank of Mexico' among the available 'Source Services'
   to choose and set the token generated in step 1.
4. If you choose 'Bank of Mexico' as a 'Source Service', the exchange
   rates will be updated from that provider.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/l10n-mexico/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/l10n-mexico/issues/new?body=module:%20currency_rate_update_banxico%0Aversion:%2017.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
-------

* Jarsa
* AMOdoo

Contributors
------------

- `Jarsa <https://www.jarsa.com>`__:

  - Alan Ramos

- `AMOdoo <https://amodoo.org/>`__

Maintainers
-----------

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/l10n-mexico <https://github.com/OCA/l10n-mexico/tree/17.0/currency_rate_update_banxico>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
