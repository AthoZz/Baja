using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;

public class Restservice : MonoBehaviour
{
    public Color startColor = Color.red;
    public Color endColor = Color.green;
    public int id_gage = 5;
    public float requestInterval = 1.0f;  // Intervalle entre les requêtes en secondes
    private float timer;

    private float value = 0;

    // Start is called before the first frame update
    void Start()
    {
        timer = requestInterval;
        //renderer = GetComponent<Renderer>();
    }

    // Update is called once per frame
    void Update()
    {
         timer -= Time.deltaTime;  // Décrémenter le timer à chaque frame

        if (timer <= 0)
        {
            string path = "http://127.0.0.1:5000/get-last-strain-gage/" + id_gage.ToString();
            Debug.Log(path);
            StartCoroutine(GetRequest(path));
            timer = requestInterval;  // Réinitialiser le timer après chaque requête
        }
        if (GetComponent<Renderer>() != null)
        {
            Renderer renderer = GetComponent<Renderer>();
            renderer.material.color = Color.Lerp(startColor, endColor, value);//Color.Lerp(startColor, endColor, value);
           
        }
    }

    IEnumerator GetRequest(string uri)
    {
        using (UnityWebRequest webRequest = UnityWebRequest.Get(uri))
        {
            // Send the request and wait for a response
            yield return webRequest.SendWebRequest();

            if (webRequest.result == UnityWebRequest.Result.ConnectionError || webRequest.result == UnityWebRequest.Result.ProtocolError)
            {
                Debug.LogError(": Error: " + webRequest.error);
            }
            else
            {
                // Show results as text
                Debug.Log(": Received: " + webRequest.downloadHandler.text);
                strain_gage_Data sensorData = JsonUtility.FromJson<strain_gage_Data>(webRequest.downloadHandler.text);
                Debug.Log("Strain Gage 5: " + sensorData.strain_gage);
                value = sensorData.strain_gage;
            }
        }
    }
}

public class strain_gage_Data
{
    public float strain_gage;
}
