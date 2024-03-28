async function main() {
    let url = prompt("Enter the URL: ");
    let url1 = "https://" + url;
    try {
        let response = await fetch(url1);
        console.log("Response code:", response.status);
        window.open(url1, '_blank');
    } catch (error) {
        console.error("Error:", error);
    }
}

main();



<script>
        // JavaScript code goes here
        async function main() {
            let url = prompt("Enter the URL: ");
            let url1 = "https://" + url;
            try {
                let response = await fetch(url1);
                console.log("Response code:", response.status);
                window.open(url1, '_blank');
            } catch (error) {
                console.error("Error:", error);
            }
        }
        
        main();
        </script>