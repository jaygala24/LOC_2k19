import cloudinary
import cloudinary.uploader
import cloudinary.api

result = Cloudinary::Uploader.upload(some_image_file_path, ocr: 'adv_ocr')

if result['info']['ocr']['adv_ocr']['status'] == 'complete'
  data = result['info']['ocr']['adv_ocr']['data']
  texts = data.map{|blocks| 
    annotations = blocks['textAnnotations'] || []
    first_annotation = annotations.first || {}
    (first_annotation['description'] || '').strip
  }.compact.join("\n")
  File.open("image_texts/#{result_['public_id']}.txt", 'w'){|f| f.write(texts)}
end
