{
    'name' : 'Caremed',
    'version':'7.0',
    'sequence': 1,
    'author' : 'Azinova Technologies pvt ltd',
    'category' : 'Azinova',
    'depends':['base','product','base_setup','report','account'],
    'update_xml':['product_change_view.xml','product_change_view.xml','account_change_view.xml',
                 'views/accounts_report.xml',
                 ],
    
    'installable':True,
    'application':True,
    'auto_install':False,
}
