using System.Collections;
using UnityEngine;
using UnityEngine.Networking;

public class RestService : MonoBehaviour
{
    public Color startColor = Color.red;
    public Color endColor = Color.green;
    public int id_gage = 5;
    public float requestInterval = 0.5f;  // Intervalle ajusté entre les requêtes en secondes
    private float value = 0;

    void Start()
    {
        StartCoroutine(RequestRoutine());
    }

    void Update()
    {
        Renderer renderer = GetComponent<Renderer>();
        if (renderer != null)
        {
            renderer.material.color = Color.Lerp(startColor, endColor, value);
        }
    }

    IEnumerator RequestRoutine()
    {
        while (true)
        {
            Debug.Log("Requête envoyée");
            string path = "https://100.107.141.200:5000/get-last-strain-gage/" + id_gage.ToString();  // Remplacez par votre URL
            yield return StartCoroutine(GetRequest(path));
            yield return new WaitForSeconds(requestInterval);  // Attendre l'intervalle spécifié avant de continuer
        }
    }

    IEnumerator GetRequest(string uri)
    {
        using (UnityWebRequest webRequest = UnityWebRequest.Get(uri))
        {
            // Ajouter la gestion des certificats pour ignorer les erreurs SSL
            webRequest.certificateHandler = new CertificateHandlerOverride();

            // Envoi de la requête et attente de la réponse
            yield return webRequest.SendWebRequest();

            if (webRequest.result == UnityWebRequest.Result.ConnectionError || webRequest.result == UnityWebRequest.Result.ProtocolError)
            {
                Debug.LogError("Erreur: " + webRequest.error);
            }
            else
            {
                // Affichage des résultats sous forme de texte
                Debug.Log("Réponse reçue: " + webRequest.downloadHandler.text);
                strain_gage_Data sensorData = JsonUtility.FromJson<strain_gage_Data>(webRequest.downloadHandler.text);
                Debug.Log("Strain Gage 5: " + sensorData.strain_gage);
                value = sensorData.strain_gage;
            }
        }
    }
}

[System.Serializable]
public class strain_gage_Data
{
    public float strain_gage;
}

public class CertificateHandlerOverride : CertificateHandler
{
    protected override bool ValidateCertificate(byte[] certificateData)
    {
        // Toujours retourner true pour ignorer les erreurs de certificat SSL.
        return true;
    }
}