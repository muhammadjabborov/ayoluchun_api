CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar_Custom': [
            {
                'name': 'document',
                'items': ('Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates')
            },
            {
                'name': 'clipboard',
                'items': ('Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo')
            },
            {'name': 'editing', 'items': ('Find', 'Replace', '-', 'SelectAll')},
            {'name': 'forms',
             'items': ('Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField')},
            '/',
            {'name': 'basicstyles',
             'items': ('Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat')},
            {'name': 'paragraph',
             'items': ('NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language')},
            {'name': 'links', 'items': ('Link', 'Unlink', 'Anchor')},
            {'name': 'insert',
             'items': (
                 'Image', 'Youtube', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak',
                 'Iframe')},
            '/',
            {'name': 'styles', 'items': ('Styles', 'Format', 'Font', 'FontSize')},
            {'name': 'colors', 'items': ('TextColor', 'BGColor')},
            {'name': 'tools', 'items': ('Maximize', 'ShowBlocks')},
            {'name': 'about', 'items': ('CodeSnippet',)},
            {'name': 'about', 'items': ('About',)},
            '/',
            {'name': 'yourcustomtools', 'items': ('Preview', 'Maximize')},
        ],
        'toolbar': 'Custom',
        'toolbarGroups': [{'name': 'document', 'groups': ('mode', 'document', 'doctools')}],
        'height': 200,
        'width': '130%',
        'filebrowserWindowHeight': 100,
        'filebrowserWindowWidth': 100,
        'toolbarCanCollapse': True,
        'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join(
            (
                'uploadimage',
                'div',
                'autolink',
                'autoembed',
                'embedsemantic',
                'autogrow',
                'devtools',
                'widget',
                'lineutils',
                'clipboard',
                'dialog',
                'dialogui',
                'elementspath',
                'codesnippet',
            )
        ),
    }
}