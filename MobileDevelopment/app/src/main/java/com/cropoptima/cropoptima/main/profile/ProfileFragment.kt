package com.cropoptima.cropoptima.main.profile

import android.content.Intent
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.cropoptima.cropoptima.R
import com.cropoptima.cropoptima.auth.AuthActivity
import com.cropoptima.cropoptima.databinding.FragmentHomeBinding
import com.cropoptima.cropoptima.databinding.FragmentProfileBinding


class ProfileFragment : Fragment() {

    private lateinit var binding: FragmentProfileBinding


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        arguments?.let {

        }
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        binding = FragmentProfileBinding.inflate(inflater, container, false)
        val root: View = binding.root

        binding.ivLogout.setOnClickListener { logout() }
        binding.tvLogout.setOnClickListener { logout() }

        return root
    }


    fun logout() {
        startActivity(Intent(binding.root.context, AuthActivity::class.java))
        return
    }
}