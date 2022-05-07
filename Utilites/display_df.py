from IPython.display import display_html
import pandas as pd
import numpy as np
class mydisplay:
    def __init__(self):
        pass
        
    def custom_display(self,dfs, names=[], index=False):
        def to_df(x):
            if isinstance(x, pd.Series):
                return pd.DataFrame(x)
            else:
                return x
        html_str = ''
        if names:
            html_str += ('<tr>' + 
                        ''.join(f'<td style="text-align:center">{name}</td>' for name in names) + 
                        '</tr>')
        html_str += ('<tr>' + 
                    ''.join(f'<td style="vertical-align:top"> {to_df(df).to_html(index=index)}</td>' 
                            for df in dfs) + 
                    '</tr>')
        html_str = f'<table>{html_str}</table>'
        html_str = html_str.replace('table','table style="display:inline"')
        display_html(html_str, raw=True)