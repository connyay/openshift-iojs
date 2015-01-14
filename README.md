# Openshift io.js

## Usage

`rhc create-app <app name> http://tinyurl.com/OpenShiftIOJS`

What this cartridge provides out of the box
---
1. **io.js** ([latest stable](http://semver.io/iojs/stable) currently 1.0.1)
2. **npm** (latest stable currently 2.1.18)
3. **grunt**
4. **bower**

What this cartridge does out of the box
---
*Not much.*

1. Installs io.js
2. Installs grunt, bower, and forever globally (specified by `$OPENSHIFT_NPM_GLOBALS`)
3. Allows the user to manually install required dependencies (in a `build` [action_hook](http://openshift.github.io/documentation/oo_user_guide.html#action-hooks)). An example of this can be found [here](template/.openshift/action_hooks/build)
4. Runs `npm start` if `package.json` is found in repo directory (log is written to `$OPENSHIFT_IOJS_LOG_DIR`)

Thanks!
---
These repos helped out a ton while developing this cartridge.

1. [engineersamuel/openshift-origin-cartridge-nodejs](https://github.com/engineersamuel/openshift-origin-cartridge-nodejs)
2. [wshearn/openshift-origin-cartridge-nodejs](https://github.com/wshearn/openshift-origin-cartridge-nodejs)
3. [ramr/nodejs-custom-version-openshift](https://github.com/ramr/nodejs-custom-version-openshift)
4. [heroku/heroku-buildpack-nodejs](https://github.com/heroku/heroku-buildpack-nodejs)
