# Ambiente básico para usar la localización Argentina con Odooenv.

Con solo bajar el odooenv y este repositorio ya podemos empezar a utilizar la localizaciòn Argentina.

La instalación es sencilla:

```
   sudo pip install odooenv
   git clone --recurse-submodules git@github.com:odoo-l10n-ar/odooenv_l10n_ar.git l10n_ar
   cd l10n_ar
   virtualenv --clear .
   odooenv install
   odooenv enable all
```

