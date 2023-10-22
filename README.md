# AI-ML-Assignment3
Create a Hinglish translation from English text. The text should sound natural and also convert all the difficult words and phrases in English to Hinglish. This converted text should be easy to understand for even a non-native Hindi speaker.
To convert this translation use the following given statements:
1. Definitely share your feedback in the comment section.
2. So even if it's a big video, I will clearly mention all the products.
3. I was waiting for my bag.
How to run code:
1.To Run this code use the Pycharm or any other compiler. Before running this code confirm that our complier must have install the the googletrans and retrying packages with the following commands:
pip install googletrans==4.0.0-rc1
pip install retrying
2. Then create the Python script in any text editor like Pycharm. And Save the file with a .py extension.
3. Then Run that python script and that shows the output of  Hinglish translation from English text.
How to evaluates its performance:
Evaluating the performance of an automated translation system, such as the one using the `googletrans` package to translate English to Hinglish, is important to ensure that the translations are accurate and meet your specific requirements. Here are some steps to evaluate its performance:

1. **Reference Translations**:
   - If possible, obtain reference translations for a set of English sentences in Hinglish. These reference translations should be done by human translators who are proficient in both languages.

2. **Evaluation Metrics**:
   - Use established evaluation metrics to compare the automated translations to the reference translations. Some common metrics for machine translation evaluation include:
     
3. **Subjective Evaluation**:
   - Gather a group of native or proficient Hinglish speakers to provide subjective evaluations of the translations. They can rate the translations based on fluency, accuracy, and overall quality. This feedback can be valuable for understanding how well the translations convey the intended meaning and whether they sound natural.

4. **Error Analysis**:
   - Examine the translations for common errors or issues. This might include incorrect word choices, grammar problems, or instances where the translation fails to capture the context of the original sentence.

5. **Domain-Specific Evaluation**:
   - Consider the specific domain or context in which the translations will be used. For example, if you're translating technical content, evaluate how well the system handles technical terms and jargon. Ensure that the translations are appropriate for your target audience and application.

6. **Data Size and Diversity**:
   - Assess whether the system performs consistently with different types of text and across a diverse range of subjects. Small datasets may lead to less accurate translations, so ensure you're evaluating it with a representative sample of text.

7. **Feedback Loop**:
   - Implement a feedback loop to continuously improve the system. Collect user feedback and use it to make necessary adjustments and refinements. Machine translation systems can be fine-tuned over time to improve their performance.

8. **Contextual Understanding**:
   - Evaluate how well the system handles context. Complex sentences, idiomatic expressions, and cultural nuances can be challenging for machine translation systems. Ensure that translations are contextually accurate.

9. **Resource Availability**:
   - Assess the availability of language resources, such as bilingual corpora, training data, and models. High-quality resources can significantly impact translation quality.

10. **Customization**:
    - Depending on your specific use case, you may have the option to fine-tune or customize machine translation models. Explore whether such customization is possible and whether it improves performance.

