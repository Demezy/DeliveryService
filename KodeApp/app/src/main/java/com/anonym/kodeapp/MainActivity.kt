package com.anonym.kodeapp

import android.annotation.SuppressLint
import android.os.Build
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.webkit.WebViewClient
import androidx.annotation.RequiresApi
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        webViewSetup()
    }
    @SuppressLint("SetJavaScriptEnabled")
    private fun webViewSetup(){
        wb_webView.webViewClient = WebViewClient()

//        change address here
        wb_webView.apply{
            loadUrl("http://192.168.1.160:8000/courier")
            settings.javaScriptEnabled = true
        }
    }

    override fun onBackPressed() {
        if (wb_webView.canGoBack()) wb_webView.goBack() else super.onBackPressed()
    }
}