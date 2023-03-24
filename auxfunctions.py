import openai
def openai_api_call(prompt: str, temperature: int = 0.5, top_p:int = 0.5, max_tokens:int = 1000) -> str:
        """
        Calls the OpenAI API with a given prompt

        Args:
            prompt (str): The prompt to use for generating the text.
        
        Returns:
            str: The generated text.
        """
        # Create the completion call using the OpenAI API
        completion_dict = openai.Completion.create(
            prompt=prompt,
            model="text-davinci-003",
            temperature=temperature,
            max_tokens= max_tokens,
            top_p = top_p
        )


        # Extract and return the generated text from the completion call response
        response_text = completion_dict['choices'][0]['text'].strip()
        return response_text