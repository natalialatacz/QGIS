"""
Przed użyciem uzupełnij pole "name" oraz sprawdzić czy "workspace" jest dobra ścieżka.
Nazwy stylów dla warstw: U.R.F, dopomiaruGPS, BNE, weryfikacja operat są domyślne.
Trzeba jedynie styl dla 'U.R.F.operaty'
"""

import os
import qgis

name = 'ObszarX'
# wkleić link do folderu docelowego zamieniajac '\' na '/'
workspace = "C:/Users/natalialatacz/Desktop/warstwyqgis"

layer1 = 'U.R.F'
layer2 = 'U.R.F_operaty'
layer3 = 'dopomiaruGPS'
layer4 = 'weryfikacja_operat'
layer5 = 'BNE'

workspace1 = f"{workspace}/{name}_{layer1}.shp"
layerFields = QgsFields()
layerFields.append(QgsField('id', QVariant.Int))
layerFields.append(QgsField('status', QVariant.String))

writer = QgsVectorFileWriter(workspace1, 'UTF-8', layerFields, QgsWkbTypes.Point,\
QgsCoordinateReferenceSystem('EPSG:2178'), 'ESRI Shapefile')
del(writer)


workspace2 = f"{workspace}/{name}_{layer2}.shp"
layerFields = QgsFields()
layerFields.append(QgsField('id', QVariant.Int))
layerFields.append(QgsField('status', QVariant.String))

writer = QgsVectorFileWriter(workspace2, 'UTF-8', layerFields, QgsWkbTypes.Point,\
QgsCoordinateReferenceSystem('EPSG:2178'), 'ESRI Shapefile')
del(writer)


workspace3 = f"{workspace}/{name}_{layer3}.shp"
layerFields = QgsFields()
layerFields.append(QgsField('id', QVariant.Int))

writer = QgsVectorFileWriter(workspace3, 'UTF-8', layerFields, QgsWkbTypes.Point,\
QgsCoordinateReferenceSystem('EPSG:2178'), 'ESRI Shapefile')
del(writer)

workspace4 = f"{workspace}/{name}_{layer4}.shp"
layerFields = QgsFields()
layerFields.append(QgsField('id', QVariant.Int))

writer = QgsVectorFileWriter(workspace4, 'UTF-8', layerFields, QgsWkbTypes.Point,\
QgsCoordinateReferenceSystem('EPSG:2178'), 'ESRI Shapefile')
del(writer)

workspace5 = f"{workspace}/{name}_{layer5}.shp"
layerFields = QgsFields()
layerFields.append(QgsField('id', QVariant.Int))

writer = QgsVectorFileWriter(workspace5, 'UTF-8', layerFields, QgsWkbTypes.Point,\
QgsCoordinateReferenceSystem('EPSG:2178'), 'ESRI Shapefile')
del(writer)


layer5 = iface.addVectorLayer(workspace5, '', 'ogr')
layer5 = iface.activeLayer()
qstyles = QgsStyle.defaultStyle()
style = qstyles.symbol('shield disability')
layer5.renderer().setSymbol(style)
layer5.triggerRepaint()
iface.layerTreeView().refreshLayerSymbology(layer5.id())

layer4 = iface.addVectorLayer(workspace4, '', 'ogr')
layer4 = iface.activeLayer()
qstyles = QgsStyle.defaultStyle()
style = qstyles.symbol('diamond green')
layer4.renderer().setSymbol(style)
layer4.triggerRepaint()
iface.layerTreeView().refreshLayerSymbology(layer4.id())

layer2 = iface.addVectorLayer(workspace2, '', 'ogr')
layer2 = iface.activeLayer()
qstyles = QgsStyle.defaultStyle()
style = qstyles.symbol('U.R.F._operaty')
layer2.renderer().setSymbol(style)
layer2.triggerRepaint()
iface.layerTreeView().refreshLayerSymbology(layer2.id())

layer1 = iface.addVectorLayer(workspace1, '', 'ogr')
layer1 = iface.activeLayer()
qstyles = QgsStyle.defaultStyle()
style = qstyles.symbol('topo hospital')
layer1.renderer().setSymbol(style)
layer1.triggerRepaint()
iface.layerTreeView().refreshLayerSymbology(layer1.id())

layer3 = iface.addVectorLayer(workspace3, '', 'ogr')
layer3 = iface.activeLayer()
qstyles = QgsStyle.defaultStyle()
style = qstyles.symbol('effect drop shadow')
layer3.renderer().setSymbol(style)
layer3.triggerRepaint()
iface.layerTreeView().refreshLayerSymbology(layer3.id())
