package com.cropoptima.cropoptima.main.setting

import androidx.lifecycle.LiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.asLiveData
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

class SettingsViewModel(private val pref: SettingsPreference) : ViewModel() {
    fun getThemeSettings(): LiveData<Boolean> {
        return pref.getThemeSetting().asLiveData()
    }

    fun saveThemeSetting(isDarkModeActive: Boolean) {
        viewModelScope.launch {
            pref.saveThemeSetting(isDarkModeActive)
        }
    }

    fun getLocale(): LiveData<String> {
        return pref.getLocaleSetting().asLiveData(Dispatchers.IO)
    }

    fun saveLocale(localeName: String) {
        viewModelScope.launch {
            pref.saveLocaleSetting(localeName)
        }
    }
}