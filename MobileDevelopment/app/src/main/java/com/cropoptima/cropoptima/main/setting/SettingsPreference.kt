package com.cropoptima.cropoptima.main.setting

import android.content.Context
import androidx.datastore.core.DataStore
import androidx.datastore.preferences.core.Preferences
import androidx.datastore.preferences.core.booleanPreferencesKey
import androidx.datastore.preferences.core.edit
import androidx.datastore.preferences.core.stringPreferencesKey
import androidx.datastore.preferences.preferencesDataStore
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

class SettingsPreference private constructor(private val dataStore: DataStore<Preferences>){
    val Context.dataStore: DataStore<Preferences> by preferencesDataStore(name = "settings")

    private val THEME_KEY = booleanPreferencesKey("theme_setting")
    private val LOCALE_KEY = stringPreferencesKey("local")

    fun getThemeSetting(): Flow<Boolean> {
        return dataStore.data.map { preferences ->
            preferences[THEME_KEY] ?: false
        }
    }

    suspend fun saveThemeSetting(isDarkModeActive: Boolean) {
        dataStore.edit { preferences ->
            preferences[THEME_KEY] = isDarkModeActive
        }
    }

    fun getLocaleSetting(): Flow<String> {
        return dataStore.data.map {
            it[LOCALE_KEY] ?: "en"
        }
    }

    suspend fun saveLocaleSetting(localeName: String) {
        dataStore.edit {
            it[LOCALE_KEY] = localeName
        }
    }


    companion object {
        @Volatile
        private var INSTANCE: SettingsPreference? = null

        fun getInstance(dataStore: DataStore<Preferences>): SettingsPreference {
            return INSTANCE ?: synchronized(this) {
                val instance = SettingsPreference(dataStore)
                INSTANCE = instance
                instance
            }
        }
    }

}