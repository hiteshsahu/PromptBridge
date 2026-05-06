import { useState } from "react";
import {
    Box,
    Button,
    Card,
    CardContent,
    CircularProgress,
    Container,
    FormControl,
    InputLabel,
    MenuItem,
    Select,
    TextField,
    Typography,
} from "@mui/material";
import SmartToyIcon from "@mui/icons-material/SmartToy";

function App() {
    const [prompt, setPrompt] = useState("");
    const [model, setModel] = useState("GPT_4O_MINI");
    const [response, setResponse] = useState("");
    const [loading, setLoading] = useState(false);

    async function sendPrompt() {
        if (!prompt.trim()) return;

        setLoading(true);
        setResponse("");

        try {
            const res = await fetch("http://localhost:8000/api/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    prompt,
                    model,
                }),
            });

            if (!res.ok) {
                throw new Error("Request failed");
            }

            const data = await res.json();
            setResponse(data.response);
        } catch (error) {
            setResponse(`Error: ${error.message}`);
        } finally {
            setLoading(false);
        }
    }

    return (
        <Container maxWidth="md">
            <Box sx={{ py: 6 }}>
                <Box sx={{ display: "flex", alignItems: "center", gap: 1, mb: 3 }}>
                    <SmartToyIcon fontSize="large" />
                    <Typography variant="h4" component="h1" fontWeight="bold">
                        PromptBridge
                    </Typography>
                </Box>

                <Card elevation={3}>
                    <CardContent>
                        <FormControl fullWidth sx={{ mb: 3 }}>
                            <InputLabel>Model</InputLabel>
                            <Select
                                value={model}
                                label="Model"
                                onChange={(event) => setModel(event.target.value)}
                            >
                                <MenuItem value="GPT_4O_MINI">GPT 4o Mini</MenuItem>
                                <MenuItem value="CHATGPT_3_5">ChatGPT 3.5</MenuItem>
                            </Select>
                        </FormControl>

                        <TextField
                            label="Prompt"
                            multiline
                            rows={8}
                            fullWidth
                            value={prompt}
                            onChange={(event) => setPrompt(event.target.value)}
                            placeholder="Ask something..."
                            sx={{ mb: 3 }}
                        />

                        <Button
                            variant="contained"
                            size="large"
                            onClick={sendPrompt}
                            disabled={loading || !prompt.trim()}
                        >
                            {loading ? (
                                <>
                                    <CircularProgress size={20} sx={{ mr: 1 }} />
                                    Thinking...
                                </>
                            ) : (
                                "Send"
                            )}
                        </Button>
                    </CardContent>
                </Card>

                {response && (
                    <Card elevation={2} sx={{ mt: 4 }}>
                        <CardContent>
                            <Typography variant="h6" gutterBottom>
                                Response
                            </Typography>

                            <Typography
                                component="pre"
                                sx={{
                                    whiteSpace: "pre-wrap",
                                    fontFamily: "monospace",
                                    backgroundColor: "#f5f5f5",
                                    p: 2,
                                    borderRadius: 1,
                                }}
                            >
                                {response}
                            </Typography>
                        </CardContent>
                    </Card>
                )}
            </Box>
        </Container>
    );
}

export default App;