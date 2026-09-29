(function (global) {
  'use strict';
  var state = global.__RASYOTREND_V11__ = global.__RASYOTREND_V11__ || { surum: '1.1.0', baslatilan: {} };
  state.claim = state.claim || function (name) {
    if (state.baslatilan[name]) return false;
    state.baslatilan[name] = true;
    return true;
  };
}(window));
