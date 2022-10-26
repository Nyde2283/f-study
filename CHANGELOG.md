# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]



## [0.2.2] - 2022-10-26

### Changed

- L'exception levée au cours d'une erreure est maintenant affichée
- Ajout / modification de code pour faciliter l'ajout des polynômes dans la prochaîne version
- f-study passe sous la license GNU GPLv3

## Fixed

- Correction de certaines fautes d'orthographe

## [0.2.1] - 2022-09-10

### Fixed

- Numéro de version mis à jour
- La valeur juste après la dernière d'un menu de sélection ne provoque plus d'erreur
- L'affichage se réinitialise correctement sur les terminaux Linux et MACOS

## [0.2.0] - 2022-09-04

### Added

- Support des nombres sous forme de fraction (ex: 1/3) https://github.com/Nyde2283/f-study/pull/16
- Ajout de la classe `Fonction` avec la méthode `display` https://github.com/Nyde2283/f-study/pull/20
- Ajout d'un message d'erreur quand le programme se stoppe pour une raison inconnue https://github.com/Nyde2283/f-study/pull/21
- Ajout de la classe `Selecteur` avec la méthode `prompt` https://github.com/Nyde2283/f-study/pull/22
- Ajout d'un menu principal permettant de quitter le programme https://github.com/Nyde2283/f-study/pull/22
- Ajout d'un message de bienvenue au lancement https://github.com/Nyde2283/f-study/pull/22

### Changed

- Les messages d'erreur s'affiche maintenant de la même manière https://github.com/Nyde2283/f-study/pull/21
- Les gestion des tableaux est maintenant plus lisible / compréhensible https://github.com/Nyde2283/f-study/pull/20
- Le message à propos des issues à la fin des tableaux a été retiré https://github.com/Nyde2283/f-study/pull/22

### Fixed

- Les nombres entiers ne se finissent plus par un `.0` dans les tableaux
- Le programme se relance de lui-même quand il est stoppé par une erreur https://github.com/Nyde2283/f-study/pull/20
- Le programme ne crash plus quand du texte est rentré lors de la définition d'une fonction https://github.com/Nyde2283/f-study/issues/18

[Unreleased]: https://github.com/Nyde2283/f-study/compare/v0.2.2...dev
[0.2.2]: https://github.com/Nyde2283/f-study/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/Nyde2283/f-study/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/Nyde2283/f-study/compare/v0.1.0...v0.2.0