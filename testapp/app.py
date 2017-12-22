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
        self.vlayout = LinearLayout(self._activity)
        self.vlayout.setOrientation(LinearLayout.VERTICAL)

        self.textbox = EditText(self._activity)
        self.vlayout.addView(self.textbox)

        self.update_text_button = Button(self._activity)
        self.update_text_button.setText('update text')
        self.update_text_button.setOnClickListener(ButtonClick(self.update_text))
        self.vlayout.addView(self.update_text_button)

        self.text_result = TextView(self._activity)
        self.text_result.setText('test')
        self.vlayout.addView(self.text_result)

        self.change_view_button = Button(self._activity)
        self.change_view_button.setText('change view')
        self.change_view_button.setOnClickListener(ButtonClick(self.change_view))
        self.vlayout.addView(self.change_view_button)
        
        self._activity.setContentView(self.vlayout)

    def update_text(self):
        text = self.textbox.getText()
        self.text_result.setText(text)

    def change_view(self):
        self.vlayout.removeAllViews()
        self.vlayout.addView(self.text_result)
        self.text_result.setText('View changed')

def main():
    MainApp()
