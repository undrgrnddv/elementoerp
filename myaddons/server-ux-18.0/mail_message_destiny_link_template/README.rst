==================================
Mail Message Destiny Link Template
==================================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:5c7e49ddc839332fe74a8bc9b0870b5bc0f543a75d572b69acb6e461a80b9bb1
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-LGPL--3-blue.png
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fserver--ux-lightgray.png?logo=github
    :target: https://github.com/OCA/server-ux/tree/18.0/mail_message_destiny_link_template
    :alt: OCA/server-ux
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/server-ux-18-0/server-ux-18-0-mail_message_destiny_link_template
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/server-ux&target_branch=18.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module provides an email template to show which target records have
been modified by a source record.

Example: When a purchase order generates an invoice, the invoice
contains a message indicating its origin with a link to the purchase
order. However, the purchase order does not log any message stating that
it has generated an invoice. This module allows developers to implement
that functionality by providing a ready-to-use template.

⚠️ This module does not add functionality by itself. It is part of the
server-ux repository and is intended for developers, who can implement
the provided template as needed. The module includes an example code
snippet to illustrate how to use it.

**Table of contents**

.. contents::
   :local:

Use Cases / Context
===================

This module has been created to obtain a reverse template of
``message_origin_link`` (which allows you to link the origin record in
the chatter).

Usage
=====

To use this module, make sure that the template you are going to write
the message inherits from ``mail.thread``.

You can call the template like this:

.. code:: python

   def custom_function(self):
       """Adds a chatter message to origin and destiny records"""
       for record in self:
           destiny_records = record._create_destiny_records()  # A bunch of Destiny Records
           mt_note_subtype_id = self.env['ir.model.data']._xmlid_to_res_id('mail.mt_note')

           # Add note to chatter that indicates destiny records
           record.message_post_with_view(
               'mail_message_destiny_link_template.message_destiny_link',
               values={'self': record, 'destiny': destiny_records, "edit": False or True},
               subtype_id=mt_note_subtype_id,
           )

           # Origin Link common usage to show differences
           for destiny_record in destiny_records:
               destiny_record.message_post_with_view(
                   'mail.message_origin_link',
                   values={'self': destiny_record, 'origin': record, "edit": False or True},
                   subtype_id=mt_note_subtype_id,
               )

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/server-ux/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/server-ux/issues/new?body=module:%20mail_message_destiny_link_template%0Aversion:%2018.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
-------

* Moduon

Contributors
------------

- Eduardo de Miguel (``Moduon <https://www.moduon.team/>``\ \_\_)

Maintainers
-----------

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-Shide| image:: https://github.com/Shide.png?size=40px
    :target: https://github.com/Shide
    :alt: Shide
.. |maintainer-rafaelbn| image:: https://github.com/rafaelbn.png?size=40px
    :target: https://github.com/rafaelbn
    :alt: rafaelbn

Current `maintainers <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-Shide| |maintainer-rafaelbn| 

This module is part of the `OCA/server-ux <https://github.com/OCA/server-ux/tree/18.0/mail_message_destiny_link_template>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
