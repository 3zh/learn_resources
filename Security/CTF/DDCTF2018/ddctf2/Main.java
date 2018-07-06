package com.example.a13251.ddctf2;

import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XC_MethodHook;
import de.robv.android.xposed.XposedBridge;
import de.robv.android.xposed.XposedHelpers;
import de.robv.android.xposed.callbacks.XC_LoadPackage;
/**
 * Created by 13251 on 2018/4/19.
 */

public class Main implements IXposedHookLoadPackage {
    @Override
    public void handleLoadPackage(XC_LoadPackage.LoadPackageParam loadPackageParam) throws Throwable {
        if (!loadPackageParam.packageName.equals("cn.chaitin.geektan.crackme")){
            return;
        }
        XposedHelpers.findAndHookMethod("java.lang.String", loadPackageParam.classLoader, "equals", Object.class, new XC_MethodHook() {
            @Override
            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
                if(param.args[0].toString().contains("DDCTF")){
                    XposedBridge.log("before"+param.args[0]);
                }

            }

            @Override
            protected void afterHookedMethod(MethodHookParam param) throws Throwable {

            }
        });
    }
}
