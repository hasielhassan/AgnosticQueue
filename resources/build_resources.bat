:: be sure to have the proper pyside2 uic on path
pyside2-uic --from-imports job_card_form.ui > ../python/ui/job_card_form.py
pyside2-uic --from-imports queue_dialog_form.ui> ../python/ui/queue_dialog_form.py
pyside2-uic --from-imports queue_overview_form.ui> ../python/ui/queue_overview_form.py

:: you actually need to replace this paths with fullpaths
:: Qt --convert doesn't support relative paths
python -m Qt --convert ../python/ui/job_card_form.py
python -m Qt --convert ../python/ui/queue_dialog_form.py
python -m Qt --convert ../python/ui/queue_overview_form.py