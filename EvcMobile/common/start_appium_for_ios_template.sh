ios_webkit_debug_proxy -u {}:27753 &
export PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin;
/Applications/Appium.app/Contents/Resources/node/bin/node /Applications/Appium.app/Contents/Resources/node_modules/appium/bin/appium.js --address "{}" --port "{}" --command-timeout "{}" --debug-log-spacing --platform-version "{}" --platform-name "{}" --app "{}" --udid "{}" --no-reset --show-ios-log --device-name "{}" --native-instruments-lib > {} &