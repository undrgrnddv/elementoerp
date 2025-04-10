# Copyright (C) 2017 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "SQL Request Abstract",
    "version": "18.0.1.0.0",
    "author": "GRAP,Akretion,Odoo Community Association (OCA)",
    "maintainers": ["legalsylvain"],
    "website": "https://github.com/OCA/reporting-engine",
    "license": "AGPL-3",
    "category": "Tools",
    "summary": "Abstract Model to manage SQL Requests",
    "depends": ["mail"],
    "data": [
        "security/ir_module_category.xml",
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "views/view_sql_request_mixin.xml",
    ],
    "assets": {
        "web._assets_core": [
            "sql_request_abstract/static/src/js/code_editor.esm.js",
        ],
        "web.ace_lib": [
            "sql_request_abstract/static/lib/ace/mode-pgsql.js",
        ],
    },
    "installable": True,
}
