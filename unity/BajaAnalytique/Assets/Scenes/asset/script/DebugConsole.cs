using System;
using System.IO;
using System.Runtime.InteropServices;
using UnityEngine;

public class DebugConsole : MonoBehaviour
{
    [DllImport("kernel32.dll", SetLastError = true)]
    private static extern bool AllocConsole();

    [DllImport("kernel32.dll", SetLastError = true)]
    private static extern bool FreeConsole();

    private TextWriter _consoleWriter;

    void Awake()
    {
        if (AllocConsole())
        {
            _consoleWriter = new StreamWriter(Console.OpenStandardOutput())
            {
                AutoFlush = true
            };
            Console.SetOut(_consoleWriter);
            Console.SetError(_consoleWriter);

            Application.logMessageReceived += HandleLog;
            Debug.Log("Console allouée.");
        }
    }

    void OnDestroy()
    {
        Application.logMessageReceived -= HandleLog;

        if (_consoleWriter != null)
        {
            Console.SetOut(TextWriter.Null);
            Console.SetError(TextWriter.Null);
            _consoleWriter.Close();
        }
        FreeConsole();
    }

    private void HandleLog(string logString, string stackTrace, LogType type)
    {
        Console.WriteLine($"{type}: {logString}");
        if (type == LogType.Exception)
        {
            Console.WriteLine(stackTrace);
        }
    }
}
