OpenERP Module Maker/Generator
==============================

OpenERP/Odoo Module which help you to Create/Generate OpenERP Module.

Just few configurations for Object, Fiels, Field type, views
and it will generate module zip file for you.
You can extract zip file put file in addons path and it is ready to install.

Benifits
--------

* No Python knowledge is required
* Hassle free OpenERP Module creation
* All field types
* Button Event
* Inheriting object

________________
Documentation
-------------

**Create a module**

![Selection_014.png](https://bitbucket.org/repo/dx7zRM/images/4226504272-Selection_014.png)

**Create Object**

![Selection_015.png](https://bitbucket.org/repo/dx7zRM/images/3888650947-Selection_015.png)

**Create Fields**

`Character Field`

![Selection_016.png](https://bitbucket.org/repo/dx7zRM/images/2708888647-Selection_016.png)

`Selection Field`

![Selection_017.png](https://bitbucket.org/repo/dx7zRM/images/4278325284-Selection_017.png)

**Setup Button for status flow**

![Selection_018.png](https://bitbucket.org/repo/dx7zRM/images/225195197-Selection_018.png)

**Generate Module by clicking `Create Module`**
![Selection_019.png](https://bitbucket.org/repo/dx7zRM/images/2767703413-Selection_019.png)


```
#!python

from openerp.osv import osv, fields

class demo_demo(osv.osv):
    _name = 'demo.demo'

    _columns = {
        'name': fields.char(size=64, string='Name', required=True, ),
        'state': fields.selection([('draft','Draft'), ('open','Open'), ('done','Done')], string='Status',  ),
    }
    def act_open(self, cr, uid, ids, conext=None):
        return self.write(cr, uid, ids, {'state': 'open'})
    def act_done(self, cr, uid, ids, conext=None):
        return self.write(cr, uid, ids, {'state': 'done'})


demo_demo()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
```


```
#!xml

        <record id="view_demo_demo_form" model="ir.ui.view">
            <field name="name">demo.demo.form</field>
            <field name="model">demo.demo</field>
            <field name="priority" eval="8"/>
            <field name="arch" type="xml">
                <form string="Demo Demo" version="7.0">
                    <header>
                        <button string="Open" name="act_open" states="draft" type="object"/>
                        <button string="Done" name="act_done" states="open" type="object"/>
                    </header>
                    <sheet>
                        <group>
                        <field name="name"/>
                        <field name="state"/>
                        </group>
                    </sheet>
                </form>
            </field>
        </record>
```