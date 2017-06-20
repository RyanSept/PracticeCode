from kivy.gesture import GestureDatabase,Gesture
from kivy.uix.boxlayout import BoxLayout
gesture_strings={'left_to_right_line': 'eNq1l0ty4zYQhve8iLUZVT/QD1zAs02VD5BybJatmonNkjSZzO3TaMqWlMQmN+CG0o/GB6D/Jghudt92f/3aPo2H44/9OHw93ScYNo8TDnc3L/d/jjfDRPEzbjwc7m4Ox/3rt/EQf8uw+T7JsPlfyF2GDZM2lEX/6XX3cmzdvHWrH3T7rUUNE84zaFP4FV2QhtsvsAWwUhixcmEVQm3z+bu1c7ZLBWBlreZmgHU4/HH/+TAlh5HhqY3QBsDC0VmYzASqQRkOT290KYLEFREIfAU8l472DkdgdNcaF0ph4jO7VPGYNSkZOPky25Nde7Apc0/4zqYi5EWxGHPDywUb0KSSU6SsSsFlOCWc+8DTTpI+8LSTbA2cqlblqBdl5KplGZ5+Uu0C5zSUsQ88DeVVhqKyFVcSUeDihZbp6ShLJ3paytaJnp5y7UMvaWpZZSrEVilkCI4WWwHhsq0lbS3cC5++FumFT2OL9cKns6V2wktaKxfWxptIIV5sUJwdxE/4aIrRyB3VMPZ/XfHKkzRWuA88bRXpA09TxfrA01JZfqHGs2oVxEzjmCCOArwI1zRUsQ88DdWToXlKAmYPaORGYj9njsy98YlLnJ8qi6ELxpazzE9PVbrx01a1C/5/TnlvcInnB0JyLbFj4gp42qr1DMcixSLr4GAWv85Fw4AablQhwrBhxYNq6avhKnocNcRDIhZ2t+W5WxprvIouqlE1Gqlht+VytzTVZBU76rDEZaTxlM3w9h3wsB/Hl/dTfSwojvVmw+a24BaGW6oUt+NkPtyfNZ61mhrPWknNoWl6irNZw6ZlwC0DtdI7X9oCqAXEvjtH1G29vEqL4BZBoB9HlIxw/DhCWgTrJxGaC6I6R/g8e0vRPpl+5kZA5kXr3C2TI+iXWayZHTmlzOcBaqYnNoorMVMS9XAlZhZknsq7mAsXv+6ea1WAK1Fn8Xp0m8VrZqxoro/ncff0fIzKqDWa8V85y0/Jn7vH43P7fIMgxIkzCKEeX7+P+/uXhzFbMHfFpp8q+fdp//r44+GYrVG8tM3dEtiiNuMLJ8pz+w+0etsD',
                 'right_to_left_line': 'eNqVmM1SI0cMx+/zInCJq/XdegHnmioeIEXAxVK7ARd4k+zbR6MmxE1CT9uXwbLm35J+mm4N149fH//4sXs4vJ6+vxyWn9+ux7Jc3x9hubl6uv39cLUcMf6MCy2vN1evp5fnr4fX+MrL9bejLNf/K3KTbstRVymL+4/Pj0+n9ba63uaf3PbL6rUcoUWwhvAjbgFc9j+VXSlALlZByQxqQfc1or9WD1r2ZcdeKgAURqikKMvrb7fjdTjXkeVhtMTDm7oYiKHUoiygyNvymT3YnDxUjd/ANcxmtq1eU92n1Kka8yXqmAgQ5tQFqIbJ0AWrbFcGMdVpTh2EqBCxVxMn2FZPrDiHlUrxchFWTKw4hxUl2lG51kpkbBPBJ1acw4qgZiGPau6lVNyUp+RKc1yhmp8FX7bbhhIszYENW72obSjB0hxYQKsXtQ0lV3rjmuJR0tYWgBVR5V/x2GYKMYBDUXWv2+rJlXxGPUCebzVlO3ZOrAxT6tJ3fOS9KZ9YmabkiwXXd6q0ItmST64s2/IrcwBxNAYn4Uqm233DSZZtTp8FWSUas3rsO2X7meJEyz4nX6uAVIhLFS11u/iSbAWm5AFQhLEWciuIE20vyVZoTl6LEmC0vpFz7Mvb8slW5thCfn8vjm0f4ZJoZQ5txB27JBMjE5iWCflEK3Nokdkui14Trc6hRY2ePEO7rZ5kdY7s+rS+tz1OPLSaYHUOLCGX7qHdlk+wOgc2TiexmEIANOY+KttbgiZYnQNLNaazWv85abaDt+Rqc1wZhOki9eRqc1w5puLLKm8J1ubAcrQjf5Rf3xPuXg6Hp/epP+wx9sfceb3XGpLLnoTicjpaXW7/a/Q0mp4ba2lG7ozQjNAZMY1aOyM1Y6/JzYidUdIo3hm1GfvVrRm74GvLiKUztozIzo3eMsJuIW8ZYReSt4yg0/SWUek1W0alK4hnRuJd8K7N2AXvmZH0ODwzkr50nhlJX5DolLTyB2vmJH32UDIp6dOHQs36ln8InX80XTLHGGN2fv7hT/0zfXYbSGYxYtSdlcw6sflAsjYXGLhkDVlpclXI6sZe97kkZKmZ68ffPvNPCLEBzYaQeBgHiQM3l0Hi0IiUkUojUsrAJSGQjxZKCLGBD1wSAtnABbPupCOXrHvr4s9cstTx1jBwyerG2DlwyeoSjlyyugQ6cMnq0ggAtuqWUUZZXfTRQt5cBklTVhfrIBaC5jJofMLmMoiFqLnIwIWbyyjcrC7aaCFtLgNGlNVFHam06o66Lt4nb9uB++Xw+PDltP4vLN4F99D7Sow74fPn4/3pS7rAsudsj7Cenr8dXm6f7g75Sx75sNrfpoNfjy/P99/vmnQc+rhTitfpGFpqPBfmtA5bu78BRQv0zw==',
                 'bottom_to_top_line': 'eNq1l89uGjEQh+/7IuFS5PnnsV8gvVbKA1QkWRGUFlZA2ubtOx7D4kppe1iZwwC/HX/e3c9izWr3uvvxvt6Op/PbcRw+X96nMKyeJxge7vab7+PdMKF9tDcaTg93p/Px8Dqe7CsPq2+TDKsPIQ/eNkyxoNTGT4fd/lyGpTIs/2XYl9I1TFDPoJzCuw0BHO4/hTUTIUbOorWW0/lVDpMfDkGIIaVQq7AMp8fNv+dhn0eG7XWKYEOVI1OtNsd2Ad6vHnTGU8QQgJGlVlqGT47PNzxqAqIcqNZFdHQHCDMdEyJmYlavcSEeHU83PEAIjErildMyvJtF6YV3s6i98G4Wb2YBEyWCHFKt13tf6IRB7LhXzWrL7X94crUEvfCulm5qAwZACAmjV0m6jO9uSbrxXS5pN77bpdyLz66XL3rNbkghcWARrxGW0d0uUye6u2XpRHezrJ3o7pXzlY6QIQtIjF51mVVxqwKd6G5VqBPdrcpslYJK8xgMC+luVbQT3a1K7kOPbjXOVimnmJAoQq0L6W41Uie6W43Sie5W42zVtmMYsm3Q1GviZXS3GnMfurpVna2KbQ9SZrH7U2paBnepSn3g7lRnp/YDoNdNjdVmYwCgNjPFS4WCLv8Pno7juJ93+xrLdt9+Plb3FNM6DPcxWz1PmobNnCmtc/vS0pDbhvxnQ7aGFJqG/AEhQdMAQT5AYNuBaLeseUHpoLaD1c/dVkcJFTzUWENpQgSuYWxDqZduj/cmzKmGqQkJL525DSN4mEMbpjpRhia0Z1kN6+Upe4ihhnZFVdXLuNu+nE1SZgNJGWrpz93z+aWEYq5qdD58G4+b/VP5L5ijPzhLfFlBX6fj4fntyUFqoLXtH0PIZWFwhLJkHte/AX/3wGY='
                 }

gestures=GestureDatabase()
for name,gesture_string in gesture_strings.items():
    gesture=gestures.str_to_gesture(gesture_string)
    gesture.name=name
    gestures.add_gesture(gesture)
class GestureBox(BoxLayout):
    def __init__(self, **kwargs):
        for name in gesture_strings:
            self.register_event_type('on_{}'.format(name))
        super(GestureBox, self).__init__(**kwargs)
    def on_touch_down(self,touch):
        touch.ud['gesture_path']=[(touch.x,touch.y)]  #ud==user data, it is passed as a dictionary.thus, a gesture_path list is created by us.
        super(GestureBox,self).on_touch_down(touch) #super method is called so widgets still work
        
    def on_touch_move(self,touch):
        touch.ud['gesture_path'].append((touch.x,touch.y))
        super(GestureBox,self).on_touch_move(touch)
    def on_touch_up(self,touch):
        if 'gesture_path' in touch.ud:
            gesture = Gesture()
            gesture.add_stroke(touch.ud['gesture_path'])
            gesture.normalize()
            match = gestures.find(gesture, minscore=0.90)
        if match:
            self.dispatch('on_{}'.format(match[1].name))
        super(GestureBox,self).on_touch_up(touch)
    def on_left_to_right_line(self):
        pass
    def on_right_to_left_line(self):
        pass
    def on_bottom_to_top_line(self):
        pass
