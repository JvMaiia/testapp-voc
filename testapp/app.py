import android
from android.widget import Button, LinearLayout, RelativeLayout, TextView, EditText
from android.view import Gravity

class ButtonClick(implements=android.view.View[OnClickListener]):
    def __init__(self, callback, *args, **kwargs):
        self.callback = callback
        self.args = args
        self.kwargs = kwargs

    def onClick(self, view: android.view.View) -> void:
        self.callback(*self.args, **self.kwargs)

class MainApp:
    def __init__(self):
        self._activity = android.PythonActivity.setListener(self)

    def onCreate(self):
        vlayout = LinearLayout(self._activity)
        vlayout.setOrientation(LinearLayout.VERTICAL)

        self.textbox = EditText(self._activity)
        vlayout.addView(self.textbox)

        self.update_text_button = Button(self._activity)
        self.update_text_button.setText('update text')
        self.update_text_button.setOnClickListener(ButtonClick(self.update_text))
        vlayout.addView(self.update_text_button)

        self.text_result = TextView(self._activity)
        self.text_result.setText('test')
        vlayout.addView(self.text_result)
        
        self._activity.setContentView(vlayout)

    def update_text(self):
        text = self.textbox.getText()
        self.text_result.setText(text)

def main():
    MainApp()
