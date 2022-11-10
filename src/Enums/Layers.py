import tensorflow as tf

from DataClasses import WidgetWrapper
from UI.CustomWidgets.Layers import (
    ConcatenateLayerWidget,
    DenseLayerWidget,
    InputLayerWidget,
)

layers = {
    "Input": WidgetWrapper(instance=tf.keras.layers.Input, widget=InputLayerWidget),
    "Dense": WidgetWrapper(instance=tf.keras.layers.Dense, widget=DenseLayerWidget),
    "Concatenate": WidgetWrapper(
        instance=tf.keras.layers.Concatenate, widget=ConcatenateLayerWidget
    ),
}
