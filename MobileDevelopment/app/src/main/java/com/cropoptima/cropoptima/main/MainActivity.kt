package com.cropoptima.cropoptima.main

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.fragment.app.Fragment
import androidx.navigation.findNavController
import androidx.navigation.ui.AppBarConfiguration
import androidx.navigation.ui.setupActionBarWithNavController
import androidx.navigation.ui.setupWithNavController
import com.cropoptima.cropoptima.R
import com.cropoptima.cropoptima.databinding.ActivityMainBinding
import com.cropoptima.cropoptima.main.detection.DetectionFragment
import com.cropoptima.cropoptima.main.home.HomeFragment
import com.cropoptima.cropoptima.main.profile.ProfileFragment
import com.google.android.material.bottomnavigation.BottomNavigationView

class
MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val navView: BottomNavigationView = binding.bottomNavigationViewHome
        val navController = findNavController(R.id.nav_host_fragment_home)

        val appBarConfiguration = AppBarConfiguration(
            setOf(
                R.id.home, R.id.detection, R.id.profile
            )
        )
        setSupportActionBar(binding.toolbar)
        setupActionBarWithNavController(navController, appBarConfiguration)
        navView.setupWithNavController(navController)
    }


}
