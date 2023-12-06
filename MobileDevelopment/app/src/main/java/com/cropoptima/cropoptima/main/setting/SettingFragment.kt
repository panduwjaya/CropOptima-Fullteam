package com.cropoptima.cropoptima.main.setting

import android.app.LocaleManager
import android.content.Context
import android.os.Build
import android.os.Bundle
import android.os.LocaleList
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.AdapterView
import android.widget.CompoundButton
import androidx.appcompat.app.AppCompatActivity
import androidx.appcompat.app.AppCompatDelegate
import androidx.core.os.LocaleListCompat
import androidx.datastore.core.DataStore
import androidx.datastore.preferences.core.Preferences
import androidx.datastore.preferences.preferencesDataStore
import androidx.fragment.app.Fragment
import androidx.lifecycle.ViewModelProvider
import androidx.navigation.Navigation
import com.cropoptima.cropoptima.databinding.FragmentSettingBinding

class SettingFragment : Fragment() {

    private var _binding: FragmentSettingBinding? = null
    private val binding get() = _binding!!

    private val Context.dataStore: DataStore<Preferences> by preferencesDataStore(name = "settings")
    private lateinit var pref: SettingsPreference
    private lateinit var viewModel: SettingsViewModel

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        _binding = FragmentSettingBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        pref = SettingsPreference.getInstance(requireContext().dataStore)
        viewModel = ViewModelProvider(requireActivity(), SettingsViewModelFactory(pref)).get(
            SettingsViewModel::class.java
        )

        binding.switchDarkMode.setOnCheckedChangeListener { _: CompoundButton?, isChecked: Boolean ->
            viewModel.saveThemeSetting(isChecked)
        }

        binding.ivArrowBack.setOnClickListener {
            Navigation.findNavController(binding.root).navigateUp()
        }

        val selectedLangPos = binding.spinnerLang.selectedItemPosition

        binding.spinnerLang.onItemSelectedListener = object : AdapterView.OnItemSelectedListener {
            override fun onNothingSelected(parent: AdapterView<*>?) {
                binding.spinnerLang.setSelection(1)
            }

            override fun onItemSelected(parent: AdapterView<*>?, view: View?, position: Int, id: Long) {
                Log.i("info", position.toString())
            }
        }

        Log.i("info", selectedLangPos.toString())

        viewModel.getThemeSettings().observe(viewLifecycleOwner) { isDarkModeActive: Boolean ->
            if (isDarkModeActive) {
                AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES)
                binding.switchDarkMode.isChecked = true
            } else {
                AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO)
                binding.switchDarkMode.isChecked = false
            }
        }

        binding.spinnerLang.apply {
            onItemSelectedListener = object : AdapterView.OnItemSelectedListener {
                override fun onItemSelected(
                    parent: AdapterView<*>?,
                    view: View?,
                    position: Int,
                    id: Long
                ) {
                    if(parent?.getItemAtPosition(position).toString() == language[1]) {
                        setLocale("in", viewModel)
                    } else {
                        setLocale("en", viewModel)
                    }
                }

                override fun onNothingSelected(parent: AdapterView<*>?) {
                }
            }
            adapter = arrayAdapter
        }

    }


    private fun setLocale(localeCode: String, viewModel: SettingsViewModel) {
        viewModel.saveLocale(localeCode)
        val context = requireContext()
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
            context.getSystemService(AppCompatActivity.LOCALE_SERVICE).let { localeManager ->
                if (localeManager is LocaleManager) {
                    localeManager.applicationLocales = LocaleList.forLanguageTags(localeCode)
                }
            }
        } else {
            AppCompatDelegate.setApplicationLocales(LocaleListCompat.forLanguageTags(localeCode))
        }
    }
}