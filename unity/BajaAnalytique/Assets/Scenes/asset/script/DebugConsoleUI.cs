using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class DebugConsoleUI : MonoBehaviour
{
    public Text consoleText;
    public int maxLines = 100;  // Nombre maximum de lignes dans la console
    private Queue<string> logQueue = new Queue<string>();

    void OnEnable()
    {
        Application.logMessageReceived += HandleLog;
    }

    void OnDisable()
    {
        Application.logMessageReceived -= HandleLog;
    }

    void HandleLog(string logString, string stackTrace, LogType type)
    {
        if (logQueue.Count >= maxLines)
        {
            logQueue.Dequeue();
        }
        logQueue.Enqueue(logString);
        consoleText.text = string.Join("\n", logQueue.ToArray());
    }
}
